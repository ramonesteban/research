class PagesController < ApplicationController
  def index
  end

  def upload_picture
    image = params[:picture]

    respond_to do |format|
      if !image.nil?
        ext = image.original_filename.split('.')[-1]
        if ext == 'jpg' || ext == 'png'
          name = Time.now.to_i
          new_filename = "#{name}.#{ext}"
          File.open(Rails.root.join('public', 'pictures', new_filename), 'wb') do |file|
            file.write(image.read)
          end
          format.html { redirect_to root_path, notice: 'Picture successfully uploaded.' }
        else
          format.html { redirect_to root_path, alert: 'Picture extension invalid.' }
        end
      else
        format.html { redirect_to root_path, alert: 'First take a picture.' }
      end
    end
  end
end
